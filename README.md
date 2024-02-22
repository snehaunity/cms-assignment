
```markdown
# Content Management System API

This is a Content Management System API built with Django REST Framework.

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd content-management-system-api
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

## Usage

### Endpoints

#### User Authentication

- `POST /login/`: User login endpoint.
  - Request Body: `{ "email": "<user-email>", "password": "<user-password>" }`

- `POST /signup/`: User signup endpoint.
  - Request Body: `{ "email": "<user-email>", "password": "<user-password>", "first_name": "<first-name>", "last_name": "<last-name>", "phone": "<phone-number>", "address": "<address>", "city": "<city>", "state": "<state>", "country": "<country>", "pincode": "<pincode>" }`

#### Content Management

- `GET /content/`: List all content items.
- `POST /content/`: Create a new content item.
  - Request Body: `{ "title": "<title>", "body": "<body>", "summary": "<summary>", "categories": ["<category1>", "<category2>"] }`
- `GET /content/<content-id>/`: Retrieve a specific content item by ID.
- `PUT /content/<content-id>/`: Update a specific content item by ID.
  - Request Body: `{ "title": "<updated-title>", "body": "<updated-body>", "summary": "<updated-summary>", "categories": ["<updated-category1>", "<updated-category2>"] }`
- `DELETE /content/<content-id>/`: Delete a specific content item by ID.

#### Searching Content

- `GET /content/?query=<search-term>`: Search for content items matching the provided search term in title, body, summary, and categories.

## Testing

To run the test cases, execute:

```bash
python manage.py test
```

