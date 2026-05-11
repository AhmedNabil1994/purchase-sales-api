import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_sales (request):
    if request.method == 'POST':
        file = request.FILES.get("file")

        if not file:
            return JsonResponse({
                "error": "No file uploaded"
            }, status=400)
        
        filename = file.name.lower()

        if filename.endswith(".csv"):
            #  to avoid inconsistency of # columns
            dataframe = pd.read_csv(file, on_bad_lines='skip')

        elif filename.endswith(".xlsx") or filename.endswith(".xls"):
            dataframe = pd.read_excel(file, header=4, engine='openpyxl')

        else:
            return JsonResponse ({
                "error":"unsupported file"
            }, status=400)

        # reads 1st 5 rows (head method)
        data = dataframe.to_dict(orient = "records")
        
        return JsonResponse({
            "sample": data[:5],
            "total_rows": len(data),
            "message": "file processed and uploaded successfully"
        })
    
    return JsonResponse({
        "error":"POST only"
    }, status = 400)
