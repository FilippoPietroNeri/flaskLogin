var alert = document.querySelector('#alert');

function login()
{
    const username = document.getElementById('username');
    const password = document.getElementById('password');

    fetch('/login/fetch', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username: username.value,
            password: password.value,
        })
    }).then((response) => response.json())
    .then((data) => {
        if (data.code == 200) {
            const user = JSON.parse(data.user)[0];
            alert.style.display = "block";
            alert.classList.remove("alert-danger");
            alert.classList.add("alert-success");
            alert.innerHTML = `Logged as <b>${user.Nome} ${user.Cognome}</b>`;
        } else if (data.code == 302) {
            alert.style.display = "block";
            alert.classList.remove("alert-success");
            alert.classList.add("alert-danger");
            alert.innerHTML = data.message;
        }
    })
}