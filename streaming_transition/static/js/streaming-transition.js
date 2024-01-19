function updateData (button, url, csrftoken) {
    var apartmentId = button.getAttribute('data-apartment-id');
    var visitId = button.getAttribute('data-visit-id');

    let bodyData = {};
    var fetchUrl = url;

    if (apartmentId) {
        bodyData = { 'apartmentId': apartmentId };
        fetchUrl += apartmentId + '/'; // append apartmentId to the fetchUrl
    } else if (visitId) {
        bodyData = { 'visitId': visitId };
        fetchUrl += visitId + '/'; // append visitId to the fetchUrl
    }

    console.log(fetchUrl); // log the fetchUrl to check if it's correct

    fetch(fetchUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken 
        },
        body: JSON.stringify(bodyData)
    })
    .then(response => response.json())
    .then(data => {
        window.location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}