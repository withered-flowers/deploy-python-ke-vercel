from fastapi import FastAPI

# Create instance
app = FastAPI()


# GET / ~ Root
# misalnya gw punya domain namanya itu adalah https://iseng.com
# GET https://iseng.com/
@app.get("/")
def fn_for_root_get_path():
    """
    Ini adalah fungsi untuk GET / yang menyatakan GET root path
    """

    return {"halo": "dunia"}


# GET /barang/angka_dari_user
@app.get("/barang/{angka_dari_user}")
def fn_get_list_barang_berdasarkan_angka_dari_user(angka_dari_user: int):
    print(f"Angka dari user adalah {angka_dari_user}")
    print(f"Tipe data dari angka adalah {type(angka_dari_user)}")

    return {"hello": "world"}


items = []


# GET /items
@app.get("/items")
def fn_lihat_items():
    return items


# POST /items
@app.post("/items")
def fn_tambah_items(barangku: dict):
    print(f"Barang dari user adalah {barangku}")
    return {"message": "Tambah items belum diimplementasikan"}
