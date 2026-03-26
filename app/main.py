# PATCH: unify onboarding compat handler to return HTTP 400 instead of 422
# Apply inside function: _save_user_onboarding_compat(...)

missing = []

if not company:
    missing.append("company")

if not profile_role:
    missing.append("profile_role")

if not user_type:
    missing.append("user_type")

if not intent:
    missing.append("intent")

if not country:
    missing.append("country")

if not language:
    missing.append("language")

if not whatsapp:
    missing.append("whatsapp")

if missing:
    raise HTTPException(
        status_code=400,
        detail={
            "message": "Missing required onboarding fields",
            "missing_fields": missing,
        },
    )
