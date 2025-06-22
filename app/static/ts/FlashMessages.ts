export class FlashMessage {
  container: HTMLElement;

  constructor(containerId: string) {
    const element = document.getElementById(containerId);
    if (!element) throw new Error(`Container #${containerId} not found`);
    this.container = element;
  }

  show(message: string, category: 'info' | 'success' | 'error' = 'info') {
    this.clear();

    const div = document.createElement('div');
    div.className = `alert alert-${category === 'error' ? 'danger' : category} mt-3`;
    div.role = 'alert';
    div.textContent = message;

    this.container.appendChild(div);

    setTimeout(() => div.remove(), 5000);
  }

  clear() {
    this.container.innerHTML = '';
  }
}
