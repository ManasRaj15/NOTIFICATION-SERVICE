const express = require('express');
const { v4: uuidv4 } = require('uuid');
const { saveNotification, getUserNotifications } = require('./dataStore');

const app = express();
app.use(express.json());

app.get('/', (req, res) => {
  res.send('📬 Notification Service is running. Use POST /notifications or GET /users/:id/notifications');
});

// Simulated instant processing of notification
app.post('/notifications', async (req, res) => {
  const { userId, type, message } = req.body;

  if (!userId || !type || !message) {
    return res.status(400).json({ error: 'Missing userId, type, or message' });
  }

  const notification = {
    id: uuidv4(),
    type,
    message,
    status: 'sent',
    timestamp: new Date()
  };

  saveNotification(userId, notification);

  console.log(`Notification sent to User ${userId}:`, message);
  res.status(200).json({ message: 'Notification sent', notification });
});

app.get('/users/:id/notifications', (req, res) => {
  const notifications = getUserNotifications(req.params.id);
  res.json({ userId: req.params.id, notifications });
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
