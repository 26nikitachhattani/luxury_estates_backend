# Luxury Estates — Backend API

A Django REST Framework backend for the Luxury Estates property showcase application. It provides REST APIs for managing property listings, serving property images, and collecting buyer inquiries submitted through the frontend.

## Features

### Property Management
- Retrieve all property listings.
- Retrieve individual property details.
- Create, update, and delete property listings.
- Store property information, including name, location, price, area, bedrooms, and description.
- Support property image uploads.

### Inquiry Management
- Accept inquiries from property detail pages.
- Store buyer name, email, phone number, message, and associated property.
- Retrieve submitted inquiries for authorized administrators.
- Associate each inquiry with the relevant property.

### API Security
- Public access to property listing and detail endpoints.
- Admin permissions for property creation, updates, and deletion.
- Public inquiry submission.
- Restricted access to the inquiry listing endpoint.

## Tech Stack

- **Language:** Python
- **Framework:** Django
- **API Framework:** Django REST Framework
- **Database:** Configured Django database
- **Image Handling:** Django media storage
- **CORS:** Django CORS Headers

## Project Structure

```text
luxury_estates_backend/
├── manage.py
├── requirements.txt
├── .env
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── properties/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
└── media/
    └── properties/
```

*Adjust the application and configuration directory names to match your actual project structure.*

## Getting Started

### Prerequisites

- Python 3.10 or later, compatible with your installed dependencies
- pip
- A configured database

### 1. Clone the repository

```bash
git clone https://github.com/26nikitachhattani/luxury_estates_backend
cd luxury_estates_backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it.

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```


### 4. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an administrator

```bash
python manage.py createsuperuser
```

Use this account for authorized administrative operations, subject to the authentication mechanism configured by the project.

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

Base URL: `http://127.0.0.1:8000/api`

| Method | Endpoint | Description | Access |
|---|---|---|---|
| GET | `/properties/` | Retrieve all properties | Public |
| GET | `/properties/{id}/` | Retrieve property details | Public |
| POST | `/properties/` | Create a property | Admin |
| PATCH | `/properties/{id}/` | Update a property | Admin |
| DELETE | `/properties/{id}/` | Delete a property | Admin |
| POST | `/properties/{id}/inquiries/` | Submit an inquiry | Public |
| GET | `/inquiries/` | Retrieve all inquiries | Admin |

*These endpoints reflect the intended API structure; verify the exact routes and permissions against your Django URL configuration.*

## Property Data

Property records may include the following fields:

- `name` — Property name
- `location` — Property location
- `price` — Property price
- `size_sqft` — Property area in square feet
- `bedrooms` — Number of bedrooms
- `description` — Property description
- `image` — Property image

## Inquiry Data

An inquiry contains:

- `name` — Buyer's name
- `email` — Buyer's email address
- `phone` — Buyer's phone number
- `message` — Inquiry message
- `property` — Associated property

The backend associates a new inquiry with the property identified in the request URL.

## Image Uploads

Property images are handled using Django's media storage.

For local development, configure `MEDIA_URL` and `MEDIA_ROOT` in Django settings and serve media files through Django when `DEBUG=True`.

For production, configure an appropriate media storage service and ensure uploaded files are handled securely.

## Frontend Integration

The frontend communicates with this backend through REST APIs. Configure the frontend's `NEXT_PUBLIC_API_URL` to point to the API base URL.

For local development, allow the frontend origin, such as `http://localhost:3000`, in Django's CORS settings.

## Security Notes

- Keep administrative endpoints protected by backend permissions.
- Do not expose secret keys or database credentials in version control.
- Validate and sanitize incoming data.
- Restrict uploaded file types and sizes.
- Configure production CORS, media storage, and HTTPS appropriately.

## License

Developed as part of the Luxury Estates property showcase and inquiry management application assignment.
