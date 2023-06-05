const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/'
);

chatSocket.onmessage = function (e) {
    const message = JSON.parse(e.data);
    displayMessage(message.message);
};

document.querySelector('#chat-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const messageInputDom = document.querySelector('#message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({ 'message': message }));
    messageInputDom.value = '';
});

function displayMessage(message) {
    const chatMessagesDom = document.querySelector('#chat-messages');
    const messageDom = document.createElement('div');
    messageDom.innerHTML = message;
    chatMessagesDom.appendChild(messageDom);
}