
// Verify promotional code
async function checkCode(body) {

    const data = {
        headers,
        body: JSON.stringify(body),
        method: 'POST'
    }

    let res = await fetch(CHECK_CODE, data)
    if (res.status === 403) {
        window.location.pathname = LOGIN_URL;
        throw {
            code: 403,
            msg: 'El usuario no está logeado'
        };
    }
    else if (res.status !== 200) {
        throw {
            code: res.status,
            msg: 'El servicio no está disponible por el momento. Intentelo más tarde'
        };
    }
    return await res.json()
}

/**
 * Set the modal button validator
 */
function setModalButton(ev) {
    const buttonHtml = `<button type="submit" class="btn btn-success">Verificar</button>`;
    const modalFooter = ev.target.querySelector('.modal-footer');
    modalFooter.innerHTML = buttonHtml;
}

/**
 * Set all styles for the valid code
 */
function validCode(ev, res) {
    $('#modalCheckCode').modal('hide');
    setModalButton(ev);
    showMessage(`¡El código es válido. Úsalo antes de que alguien más lo use!`);

    const formResume = document.getElementById('formResume');
    formResume.innerHTML += `<input type="hidden" name="code" value="${res.code}">`;

    document.querySelector('[data-target="#modalCheckCode"]').style.display = 'none';

    // Set new price
    const elementPrice = document.getElementById('price');
    elementPrice.firstElementChild.classList.add('text-muted');
    elementPrice.firstElementChild.style.textDecoration = 'line-through';

    if (res.price <= 0) {
        elementPrice.innerHTML += `<span class="text-success"> GRATIS</span>`;
    } else {
        elementPrice.innerHTML += `<span class="text-danger"> \$${res.price}</span>`;
    }
}

/**
 * Set all styles for the in valid code
 */
function invalidCode(ev) {
    $('#modalCheckCode').modal('hide');
    setModalButton(ev);
}


async function onSubmitCheckCode(ev) {
    ev.preventDefault();
    const spinnerHtml = `<div class="spinner-border" role="status">
                        <span class="sr-only">Loading...</span>
                        </div>`;
    const modalFooter = ev.target.querySelector('.modal-footer');
    modalFooter.innerHTML = spinnerHtml;

    const formData = new FormData(ev.target);
    const data = Object.fromEntries(formData);

    try {
        let res = await checkCode(data);
        validCode(ev, res);
    } catch (error) {
        invalidCode(ev);
        if (error.code == 400) {
            showMessage('El código no es válido :C', 'danger');
        }
        else if (error.code !== 403) {
            showMessage(error.msg, 'danger');
        }
    }
}


document.querySelectorAll('.check-code').forEach(element => {
    element.addEventListener('submit', onSubmitCheckCode);
});
