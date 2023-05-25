import { createQueue } from 'kue';

// Create a queue with Kue
const queue = createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '123456789',
  message: 'Hello, this is a notification.',
};

// Create a queue named push_notification_code and create a job
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log('Notification job created:', job.id);
    }
  });

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});

