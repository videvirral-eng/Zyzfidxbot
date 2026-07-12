from aiogram.fsm.state import State, StatesGroup


# =========================
# GET FILE
# =========================
class GetFileState(StatesGroup):
    wait_code = State()


# =========================
# UPLOAD FILE
# =========================
class UploadState(StatesGroup):
    wait_done = State()          # Menunggu tombol Done
    wait_redirect = State()      # On / Off redirect
    wait_title = State()         # Judul atau Skip
    wait_price_type = State()    # Free / Paid
    wait_price = State()         # Nominal jika Paid
    processing = State()         # Membuat code

# =========================
# ADMIN
# =========================
class AdminState(StatesGroup):
    wait_broadcast = State()
    wait_user = State()
    wait_file = State()
    wait_price = State()
    wait_confirm = State()


# =========================
# PAYMENT (BayarGG)
# =========================
class PaymentState(StatesGroup):
    wait_invoice = State()
    wait_callback = State()
