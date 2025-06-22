var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
import { FlashMessage } from "./FlashMessages";
const form = document.querySelector("#registerForm");
const flash = new FlashMessage('flash-messages');
function submitForm() {
    return __awaiter(this, void 0, void 0, function* () {
        const formData = {
            username: form.elements.namedItem('username').value.trim(),
            email: form.elements.namedItem('email').value.trim(),
            password: form.elements.namedItem('password').value.trim(),
        };
        try {
            const response = yield fetch('api/auth/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData),
            });
            const result = yield response.json();
            if (response.ok && result.success) {
                flash.show(result.message || 'Registrado com sucesso', 'success');
                form.reset();
            }
            else {
                flash.show(result.error || 'Erro inesperado', 'error');
            }
        }
        catch (_a) {
            flash.show('Erro de conexão', 'error');
        }
    });
}
form.addEventListener("submit", (e) => {
    e.preventDefault();
    submitForm();
});
