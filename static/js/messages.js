
import { htmlToElement } from './utils';


function getElementMessage(message, type='success') {
    const template = `
        <div class="alert alert-${type} alert-dismissible fade show fixed-top m-4" role="alert">
        <p>${message}</p>
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
    `;

    return htmlToElement(template);
}

function showMessage(message, type='success') {
    const element = getElementMessage(message, type);
    document.body.appendChild(element)
}

export {
    getElementMessage,
    showMessage
}