from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from rest_framework.exceptions import ValidationError


def validate_file_extension(value):
    try:
        load_workbook(value)
    except InvalidFileException as err:
        raise ValidationError(
            {
                "detail": "Invalid Uploaded file extension",
                "code": "invalid_file_extension_failed",
            }
        ) from err
    except:
        raise ValidationError(
            {"detail": "File uploaded failed", "code": "unknown_error"}
        )
