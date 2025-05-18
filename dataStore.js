const store = {};

function saveNotification(userId, notification) {
  if (!store[userId]) {
    store[userId] = [];
  }
  store[userId].push(notification);
}

function getUserNotifications(userId) {
  return store[userId] || [];
}

module.exports = { saveNotification, getUserNotifications };
