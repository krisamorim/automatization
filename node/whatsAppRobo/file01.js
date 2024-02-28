const qrcode = require('qrcode-terminal');

const { client } = require('whatsapp-web.js');
const client = new client();

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
    console.log('client is ready!');
});

client.initialize();

