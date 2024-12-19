# How to run
To run this project use build-in virtual environment and run command `uvicorn main:app --reload`.
Keep in mind that all changes you make will not be saved as this version of project does not support database integration. 

### /create
POST request for /create 
```
fetch('http://127.0.0.1:8000/create', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json', 
    },
    body: JSON.stringify({
        Concept: 'javascript', 
        Definition: 'A programming language commonly used for web development.' 
    })
})
.then(response => response.json()) 
.then(data => console.log(data)) 
.catch(error => console.error('Error:', error)); 
```

### /update
PUT request for /update/{definition}
Replace {definition} with definition name
```
fetch('http://127.0.0.1:8000/update/javascript', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json', 
    },
    body: JSON.stringify({
        NewDefinition: 'New definition of javascript is awesome!' 
    })
})
.then(response => response.json()) 
.then(data => console.log(data)) 
.catch(error => console.error('Error:', error));
```

### /remove
DELETE request for /remove/{definition
Replace {definition} with definition name
```
fetch('http://127.0.0.1:8000/remove/javascript', {
    method: 'DELETE',
    headers: {
        'Content-Type': 'application/json', 
    }
})
.then(response => response.json()) 
.then(data => console.log(data)) 
.catch(error => console.error('Error:', error));
```