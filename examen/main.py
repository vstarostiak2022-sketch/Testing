def get_file_extension(filename: str) -> str:
    if filename.startswith('.') and filename.count('.') == 1:
        return ''
    parts = filename.rsplit('.', 1)
    if len(parts) == 2 and parts[1]:
        return parts[1]
    return ''