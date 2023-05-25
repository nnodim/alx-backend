function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((job) => {
    const pushNotification = queue.create('push_notification_code_3', job);

    pushNotification
      .on('enqueue', () => {
        console.log(`Notification job created: ${pushNotification.id}`);
      })
      .on('complete', () => {
        console.log(`Notification job ${pushNotification.id} completed`);
      })
      .on('failed', (error) => {
        console.log(`Notification job ${pushNotification.id} failed: ${error}`);
      })
      .on('progress', (progress, data) => {
        console.log(`Notification job ${pushNotification.id} ${progress}% complete`);
      });

    pushNotification.save((error) => {
      if (!error) console.log(`Notification job created: ${job.id}`);
    });
  });
}
module.exports = createPushNotificationsJobs;
