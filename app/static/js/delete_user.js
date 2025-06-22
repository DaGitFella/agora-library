var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
import { FlashMessage } from "./FlashMessages.js";
const delete_btn = document.querySelector("#deleteBtn");
const flash = new FlashMessage('flash-messages');
function handleDelete() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const response = yield fetch('/api/users/delete', {
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
delete_btn === null || delete_btn === void 0 ? void 0 : delete_btn.addEventListener('click', () => {
    handleDelete();
});
