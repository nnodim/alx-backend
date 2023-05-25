import { createQueue } from 'kue';

const blacklist = ['4153518780', '4153518781'];

const queue = createQueue();
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Track progress: 0%

  if (blacklist.includes(phoneNumber)) {
    // Phone number is blacklisted
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  } else {
    job.progress(50, 100); // Track progress: 50%
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

// Process jobs from the push_notification_code_2 queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
