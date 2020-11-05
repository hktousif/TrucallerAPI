#TruecallerAPI

##Install dependencies

    pip freeze > requirements.txt
    Python manage.py makemigrations
    Python manage.py migrate
    Python manage.py runserver

##API endpoints

**Note:** username field is used as phone no field
#####Registration

    /registration/ (POST)
    -username
    -password1
    -password2
    -email
    Returns Token key

#####LogIn

    /accounts/login/
    -username
    -email
    -password
    Returns Token key
    
#####Log Out

    /accounts/logout/
    Returns HTTP 200 OK
    
#####User

    accounts/user/ (GET, PUT, PATCH)
    -username
    -first_name
    -last_name
    Returns pk, username, email, first_name, last_name

#####Create new contact

    / (POST)
    name: "",
    phone: "",
    email: "",
    isSpam: Boolean

#####Update Contact

    / (PUT)
    name: "",
    phone: "",
    email: "",
    isSpam: Boolean

#####Get Contact

    / (GET)
    id: 25,
    url: "http://127.0.0.1:8000/09945456981/",
    phone: "09945456981",
    isSpam: false,
    email: "" --- if the person is a registered user and the user who is searching is in the
                    person’s contact list.
    nameList: [
        {
            "id": 4,
            "name": "Tousif Kalalakond"
        }
    ]

#####Search Contacts

    /search/?value=Tousif (GET)
        [
            {
                "id": 26,
                "url": "http://127.0.0.1:8000/09945456989/",
                "phone": "09945456989",
                "isSpam": false,
                "nameList": [
                    {
                        "id": 6,
                        "name": "Kalalakond"
                    }
                ]
            },
            {
                "id": 25,
                "url": "http://127.0.0.1:8000/09945456981/",
                "phone": "09945456981",
                "isSpam": false,
                "nameList": [
                    {
                        "id": 4,
                        "name": "Tousif Kalalakond"
                    }
                ]
            },
    ]