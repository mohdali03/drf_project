# Django git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:mohdali03/drf_project.git
git push -u origin main

This project is built using Django and Django REST Framework (DRF) to provide CRUD operations (Create, Read, Update, Delete) through RESTful APIs.

## Features

- **CRUD Operations:** Create, retrieve, update and delete records.
- **CRUD Snippets:** Ready-to-use code snippets for quickly implementing endpoints.
- **Enhanced Project Setup:** Modular design that can be extended with additional features.

## Project Setup

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the Server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Sample CRUD Endpoints

- **List & Create:**  
  URL: `/api/items/`
  
  ```python
  from rest_framework import generics
  from .models import Item
  from .serializers import ItemSerializer

  class ItemListCreateView(generics.ListCreateAPIView):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer
  ```

- **Retrieve, Update & Delete:**  
  URL: `/api/items/<int:pk>/`
  
  ```python
  from rest_framework import generics

  class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer
  ```

### Example Serializer

```python
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
     class Meta:
          model = Item
          fields = ['id', 'name', 'description', 'created_at']
```

### Example Model

```python
from django.db import models

class Item(models.Model):
     name = models.CharField(max_length=255)
     description = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.name
```

## Additional Enhancements

- **Authentication:** Integrate token or JWT-based authentication for secure access.
- **Filtering and Pagination:** Use DRF's filter backend and pagination classes to manage large datasets.
- **Documentation:** Generate API docs using tools like drf-yasg or Swagger UI.
- **Testing:** Write unit and integration tests to ensure API reliability.

## Running Tests

Run tests using:

```bash
python manage.py test
```

## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/fooBar`
3. Commit your changes: `git commit -m 'Add some fooBar'`
4. Push to the branch: `git push origin feature/fooBar`
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.
## Snippet CRUD Operations

This section documents the API endpoints for performing CRUD operations on the Snippet model.

### Endpoints

- **List & Create Snippets:**  
    URL: `/api/snippets/`  
    Use this endpoint to retrieve all snippets or create a new snippet.

    ```python
    from rest_framework import generics
    from .models import Snippet
    from .serializers import SnippetSerializer

    class SnippetListCreateView(generics.ListCreateAPIView):
            queryset = Snippet.objects.all()
            serializer_class = SnippetSerializer
    ```

- **Retrieve, Update & Delete a Snippet:**  
    URL: `/api/snippets/<int:pk>/`  
    Use this endpoint to retrieve a specific snippet by its primary key, update its details, or delete it.

    ```python
    from rest_framework import generics

    class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
            queryset = Snippet.objects.all()
            serializer_class = SnippetSerializer
    ```

### Example Serializer for Snippet

Below is an example serializer for the Snippet model. Customize the fields as required.

```python
from rest_framework import serializers
from .models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
        class Meta:
                model = Snippet
                fields = ['id', 'created', 'title', 'code', 'linenos', 'language', 'style']
```

### Model Reference

For context, the Snippet model is structured as follows:

```python
from django.db import models

class Snippet(models.Model):
        created  = models.DateField(auto_now_add=True)
        title = models.CharField(max_length=100, blank=True, default="Defualt Title")
        code = models.TextField()
        linenos = models.BooleanField(default=False)
        language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
        style = models.CharField(choices=STYLE_CHOICES, default='freindly', max_length=100)
        
        class Meta:
                ordering = ['created']
```

Ensure you configure your URL routing to include these endpoints so they can be accessed via the defined URLs.