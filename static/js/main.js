
function login()
{
    const username = document.getElementById('username');
    const password = document.getElementById('password');

    fetch('https://3246-filippopietr-flasklogin-yqyywfzh7xl.ws-eu111.gitpod.io/login/fetch', {
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
        console.log(data);
    })
}