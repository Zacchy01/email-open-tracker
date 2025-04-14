const express = require("express");
const axios = require("axios");
const app = express();
const PORT = process.env.PORT || 3000;

// Replace with your actual bot token and chat ID
const BOT_TOKEN = "8182919246:AAEqAvPr12ZFtJJQDHEl1pn5bfSZmMSb0PM";
const CHAT_ID = "6684889364";

app.get("/email-open", async (req, res) => {
  const message = `📬 Email opened!\n🕒 Time: ${new Date().toLocaleString()}\n🌐 IP: ${req.ip}`;

  try {
    await axios.get(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
      params: {
        chat_id: CHAT_ID,
        text: message,
      },
    });

    // Return a 1x1 transparent GIF
    const img = Buffer.from(
      "R0lGODlhAQABAAAAACH5BAEAAAAALAAAAAABAAEAAAIA",
      "base64"
    );
    res.set("Content-Type", "image/gif");
    res.send(img);
  } catch (error) {
    console.error("Failed to notify:", error);
    res.status(500).send("Error");
  }
});

app.listen(PORT, () => {
  console.log(`Tracking pixel server running on port ${PORT}`);
});
