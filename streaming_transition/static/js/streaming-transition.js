function updateData (button, url, csrftoken) {
    var apartmentId = button.getAttribute('data-apartment-id');
    var fetchUrl = url + apartmentId + '/'; 

    fetch(fetchUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken 
        },
        body: JSON.stringify({ 'apartmentId': apartmentId })
    })
    .then(response => response.json())
    .then(data => {
        window.location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}