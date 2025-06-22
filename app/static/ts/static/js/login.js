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
const form = document.querySelector("#loginForm");
const flash = new FlashMessage('flash-messages');
function submitLogin() {
    return __awaiter(this, void 0, void 0, function* () {
        const formData = {
            email: form.elements.namedItem('email').value.trim(),
            password: form.elements.namedItem('password').value.trim(),
        };
        try {
            const response = yield fetch('api/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData),
            });
            const result = yield response.json();
            if (response.ok && result.success) {
                flash.show(result.message || 'Usuário logado com sucesso!');
                form.reset();
            }
            else {
                flash.show(result.message || 'Erro inesperado', 'error');
            }
        }
        catch (_a) {
            flash.show('erro inesperado', 'error');
        }
    });
}
form.addEventListener('submit', (e) => {
    e.preventDefault();
    submitLogin();
});
