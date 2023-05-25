import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';
import express from 'express';

// Create Redis client
const redisClient = createClient();

redisClient.on('connect', function () {
  console.log('Redis client connected to the server');
});

redisClient.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Promisify Redis client.get function
const asyncGet = promisify(redisClient.get).bind(redisClient);

// Reserve a seat by setting the available_seats key
function reserveSeat(number) {
  redisClient.set('available_seats', number);
}

// Get the current number of available seats
async function getCurrentAvailableSeats() {
  const seats = await asyncGet('available_seats');
  return seats;
}

let reservationEnabled = true;

// Create Kue queue
const queue = createQueue();

// Create express app
const app = express();

// Route to get the number of available seats
app.get('/available_seats', async function (req, res) {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', function (req, res) {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat', { seat: 1 }).save((error) => {
    if (error) {
      res.json({ status: 'Reservation failed' });
      return;
    } else {
      res.json({ status: 'Reservation in process' });
      job.on('complete', function () {
        console.log(`Seat reservation job ${job.id} completed`);
      });
      job.on('failed', function (error) {
        console.log(`Seat reservation job ${job.id} failed: ${error}`);
      });
    }
  });
});

// Route to process the queue
app.get('/process', function (req, res) {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async function (job, done) {
    const seat = Number(await getCurrentAvailableSeats());
    if (seat === 0) {
      reservationEnabled = false;
      done(Error('Not enough seats available'));
    } else {
      reserveSeat(seat - 1);
      done();
    }
  });
});

const port = 1245;
app.listen(port, () => {
  console.log(`App is listening at http://localhost:${port}`);
});

// Initialize the number of available seats
reserveSeat(50);

