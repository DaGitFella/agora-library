var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var _a, _b, _c;
import { FlashMessage } from "./FlashMessages.js";
const form = document.getElementById('profileForm');
const delete_btn = document.querySelector("#deleteBtn");
const flash = new FlashMessage('flash-messages');
const submitBtn = document.querySelector("#submitBtn");
const initialData = {
    username: (_a = form.elements.namedItem('username')) === null || _a === void 0 ? void 0 : _a.value.trim(),
    email: (_b = form.elements.namedItem('email')) === null || _b === void 0 ? void 0 : _b.value.trim(),
    password: (_c = form.elements.namedItem('password')) === null || _c === void 0 ? void 0 : _c.value.trim(),
};
function handleDelete() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const response = yield fetch('/api/users/me', {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({})
            });
            const result = yield response.json();
            if (result.success && response.ok) {
                window.location.href = "/";
            }
            else {
                flash.show(result.message || 'Erro ao deletar usuário', 'error');
            }
        }
        catch (_a) {
            flash.show('erro inesperado', 'error');
        }
    });
}
function handleUpdate() {
    return __awaiter(this, void 0, void 0, function* () {
        var _a, _b, _c;
        const formData = {
            username: ((_a = form.elements.namedItem('username')) === null || _a === void 0 ? void 0 : _a.value.trim()) || '',
            email: ((_b = form.elements.namedItem('email')) === null || _b === void 0 ? void 0 : _b.value.trim()) || '',
            password: ((_c = form.elements.namedItem('password')) === null || _c === void 0 ? void 0 : _c.value.trim()) || '',
        };
        try {
            const response = yield fetch('/api/users/me', {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            const result = yield response.json();
            if (result.success && response.ok) {
                flash.show(result.message || 'Atualizado com sucesso', 'success');
            }
            else {
                flash.show(result.error || 'Erro inesperado', 'error');
            }
        }
        catch (e) {
            flash.show('erro inesperado', 'error');
        }
    });
}
function checkChanges() {
    var _a, _b, _c;
    const currentData = {
        username: ((_a = form.elements.namedItem('username')) === null || _a === void 0 ? void 0 : _a.value.trim()) || "",
        email: ((_b = form.elements.namedItem('email')) === null || _b === void 0 ? void 0 : _b.value.trim()) || "",
        password: ((_c = form.elements.namedItem('password')) === null || _c === void 0 ? void 0 : _c.value.trim()) || "",
    };
    const changed = currentData.username !== initialData.username ||
        currentData.email !== initialData.email ||
        currentData.password !== initialData.password;
    submitBtn.disabled = !changed;
}
delete_btn === null || delete_btn === void 0 ? void 0 : delete_btn.addEventListener('click', () => {
    handleDelete();
});
form.addEventListener('submit', (e) => {
    e.preventDefault();
    handleUpdate();
});
form.addEventListener('input', checkChanges);
