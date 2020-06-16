
import { getCookie } from './utils';
import { showMessage } from './messages';
import { ADD_PRODUCT_URL, LOGIN_URL } from './config';


async function addProduct(body) {
    const headers = {
        credentials: 'include',
        'X-CSRFToken': getCookie('csrftoken'),
        'Content-Type': 'application/json',
    }

    const data = {
        headers,
        body: JSON.stringify(body),
        method: 'POST'
    }
    let res = await fetch(ADD_PRODUCT_URL, data)
    if (res.status === 403) {
        window.location.pathname = LOGIN_URL;
        throw {
            code: 403,
            msg: 'El usuario no está logeado'
        };
    }
    else if (res.status !== 201) {
        throw {
            code: res.status,
            msg: 'El servicio no está disponible por el momento. Intentelo más tarde'
        };
    }
    return await res.json()
}


async function addProductWidget(ev) {
    ev.preventDefault();
    const button = ev.target.querySelector('[type=submit]');
    button.setAttribute('disabled', true);
    const formData = new FormData(ev.target);
    const data = Object.fromEntries(formData);
    try {
        await addProduct(data);
        showMessage(
            `¡Se ha agreado un producto a tu
            <a class="font-weight-bold" href="/carrito/">carrito</a>!
        `);
        button.removeAttribute('disabled');
    } catch (error) {
        if (error.code !== 403) {
            showMessage(error.msg, 'danger');
        }
    }
}

document.querySelectorAll('.cart-product-widget').forEach(element => {
    element.addEventListener('submit', addProductWidget);
});
