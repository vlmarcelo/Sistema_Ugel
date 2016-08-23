# -*- encoding: utf-8 -*-
from django.views.generic import ListView
from spreadsheetresponsemixin import SpreadsheetResponseMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin
from braces.views import StaffuserRequiredMixin
from braces.views import SuperuserRequiredMixin
from braces.views import MultiplePermissionsRequiredMixin
from braces.views import AnonymousRequiredMixin
from braces.views import RecentLoginRequiredMixin


class ExcelExportView(SpreadsheetResponseMixin, ListView):
    def get(self, request):
        self.queryset = self.get_queryset()
        return self.render_excel_response()

    class Meta:
    	exclude = ('username')

class CsvExportView(SpreadsheetResponseMixin, ListView):
    def get(self, request):
        self.queryset = self.get_queryset()
        return self.render_csv_response()


class AccessUserRequiredMixin(LoginRequiredMixin, MultiplePermissionsRequiredMixin):
	#10 minutos
	#max_last_login_delta = 600  
	#LoginRequiredMixin
	login_url	  = reverse_lazy('usuario:login')
	#MultiplePermissionsRequiredMixin
	permissions   = {
		'all':( 'grupos_sanguineos.add_grupo_sanguineo', 
				'grupos_sanguineos.change_grupo_sanguineo', 
				'grupos_sanguineos.delete_grupo_sanguineo'),
	}
    


       

