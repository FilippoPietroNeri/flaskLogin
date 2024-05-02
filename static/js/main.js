
function loginInfo()
{
    const username = document.getElementById('username');
    const password = document.getElementById('password');

    fetch('https://3246-filippopietr-flasklogin-zeuacy53xgb.ws-eu110.gitpod.io/login', {
        method: 'POST',
        body: {
            username,
            password
        }
    }).then((response) => response.json())
    .then((data) => {
        console.log(data);
    })
}