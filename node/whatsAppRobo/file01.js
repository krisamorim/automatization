// https://youtu.be/cMsC7a9ToDk
const qrcode = require('qrcode-terminal');

const { client } = require('whatsapp-web.js');
const client = new client();

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
    console.log('client is ready!');
});

client.on('message', message =>{
    if(message.body.toLocaleLowerCase() === 'Olá'){
        client.sendMessage(message.from, 'Me chamo XXXX');
        client.sendMessage(message.from, 'Como popsso ajudar?\n1- Status\n2-Outros');
    }

    if(message.body.toLocaleLowerCase() === '1'){
        client.sendMessage(message.from, 'Finalizado');
    }

    if(message.body.toLocaleLowerCase() === '2'){
        client.sendMessage(message.from, 'Não tem outros');
    }

})

client.initialize();

