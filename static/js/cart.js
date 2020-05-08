

const headers = {
    credentials: 'include',
    'X-CSRFToken': getCookie('csrftoken'),
    'Content-Type': 'application/json',
}

async function addProduct(body) {
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

async function addProductButton(button) {
    const product_id = parseInt(button.dataset.product_id);
    button.setAttribute('disabled', true);

    try {
        let res = await addProduct({product: product_id});
        showMessage('¡Se ha agreado un producto a tu carrito!');
        button.removeAttribute('disabled');
    } catch (error) {
        if (error.code !== 403) {
            showMessage(error.msg, 'danger');
        }
    }
}
