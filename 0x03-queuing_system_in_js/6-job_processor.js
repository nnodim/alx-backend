import { createQueue } from 'kue';

// queue with Kue
const queue = createQueue();

// function to send notifications
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process new jobs on the push_notification_code queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message);

  done();
});

