var url = 'http://localhost:5001/'
fetch(url, {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    //mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    //credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'text/plain'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    //redirect: 'follow', // manual, *follow, error
    //referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
}).then(response => {
  console.log('ok', response.ok, response.status, response.statusText)
  if (response.ok) {
    response.text().then(t => { console.log(t) })
  }
}).catch(e => {
  console.log(e.message)
})

var url = 'http://localhost:5001/'
fetch(url, {
    method: 'GET',
    cache: 'no-cache',
    headers: { 'Content-Type': 'text/plain' },
})
.then(response => { console.log(response.status, response.statusText, response.text()) })
.catch(e => { console.log(e) })

var url = 'http://localhost:5001/cors'
fetch(url, {
    method: 'GET',
    cache: 'no-cache',
    headers: { 'Content-Type': 'text/plain' },
})
.then(response => { console.log(response.status, response.statusText, response.text()) })
.catch(e => { console.log(e) })

var url = 'http://localhost:5001/cors-auth'
fetch(url, {
    method: 'GET',
    cache: 'no-cache',
    headers: { 'Content-Type': 'text/plain', 'Authorization': `Basic ${btoa('john:hello')}` },
})
.then(response => { console.log(response.status, response.statusText, response.text()) })
.catch(e => { console.log(e) })