from rest_framework import viewsets
from store.models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned products to a given category,
        by filtering against a `category` query parameter in the URL.
        This now maps the display name from Flutter (e.g., 'Electronics')
        back to the short code (e.g., 'EL') stored in the model.
        """
        queryset = Product.objects.all()
        category_display_name = self.request.query_params.get('category', None)

        if category_display_name is not None and category_display_name.lower() != 'all' and category_display_name != '':
            # Convert the incoming display name (e.g., "Electronics")
            # to the stored code (e.g., "EL") using CATEGORY_CHOICES.
            # We iterate through the choices to find a match.
            target_category_code = None
            for code, display_name in Product.CATEGORY_CHOICES:
                if display_name.lower() == category_display_name.lower():
                    target_category_code = code
                    break # Found the matching code

            if target_category_code:
                # Filter the queryset by the actual 'category' field using the found code
                queryset = queryset.filter(category=target_category_code)
            else:
                # If the incoming category display name doesn't match any choices,
                # return an empty queryset or handle as an error.
                # For now, we'll return an empty queryset to signify no matches.
                queryset = queryset.none()


        # Always order randomly, even if filtered by category,
        # unless a different ordering is desired for filtered sets.
        return queryset.order_by('?')

    def get_serializer_context(self):
        return {'request': self.request}