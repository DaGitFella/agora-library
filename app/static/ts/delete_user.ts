import {FlashMessage} from "./FlashMessages";

const delete_btn = document.querySelector("#deleteBtn");
const flash = new FlashMessage('flash-messages');

async function handleDelete() {
    try {
        const response = await fetch('/api/users', {
            method: 'DELETE',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({})
        });

        const result = await response.json();

        if (result.success && response.ok) {
            window.location.href="/";
        } else {
            flash.show(result.message || 'Erro ao deletar usuário', 'error');
        }
    } catch {
        flash.show('erro inesperado', 'error');
    }
}

delete_btn?.addEventListener('click', () => {
    handleDelete();
})