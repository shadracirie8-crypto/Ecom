from django import forms

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:

        model = Order

        fields = [

            'full_name',

            'phone',

            'email',

            'city',

            'commune',

            'address',

            'note',

            'payment_method'

        ]

        widgets = {

            'full_name': forms.TextInput(attrs={

                'class': 'w-full h-14 rounded-2xl border border-gray-200 px-5 outline-none focus:border-indigo-500',

                'placeholder': 'Nom complet du receveur'

            }),

            'phone': forms.TextInput(attrs={

                'class': 'w-full h-14 rounded-2xl border border-gray-200 px-5 outline-none focus:border-indigo-500',

                'placeholder': 'Numéro téléphone'

            }),

            'email': forms.EmailInput(attrs={

                'class': 'w-full h-14 rounded-2xl border border-gray-200 px-5 outline-none focus:border-indigo-500',

                'placeholder': 'Adresse email'

            }),

            'city': forms.TextInput(attrs={

                'class': 'w-full h-14 rounded-2xl border border-gray-200 px-5 outline-none focus:border-indigo-500',

                'placeholder': 'Ville'

            }),

            'commune': forms.TextInput(attrs={

                'class': 'w-full h-14 rounded-2xl border border-gray-200 px-5 outline-none focus:border-indigo-500',

                'placeholder': 'Commune'

            }),

            'address': forms.Textarea(attrs={

                'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4 outline-none focus:border-indigo-500',

                'rows': 4,

                'placeholder': 'Adresse complète de livraison'

            }),

            'note': forms.Textarea(attrs={

                'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4 outline-none focus:border-indigo-500',

                'rows': 3,

                'placeholder': 'Note supplémentaire (optionnel)'

            }),

            'payment_method': forms.Select(attrs={

                'class': 'w-full h-14 rounded-2xl border border-gray-200 px-5 outline-none focus:border-indigo-500'

            }),

        }