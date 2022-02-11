function enterKeyPress(event) {
	if (event.keyCode !== 13) {
		return false;
	}
	return true;
}

function createNewAccountNode(new_account) {
	const div = document.createElement("DIV");
	const p = document.createElement("P")
	const strong = document.createElement("STRONG");
	strong.innerText = new_account;
	p.appendChild(strong);
	div.appendChild(p);
	// NOTE: accounts node children has been swapped so taking the 0-th index
	const parent_node = document.getElementById("accounts").children[0];
	parent_node.insertBefore(div, parent_node.children[0]);
}

function registerNewAccount(event) {
	const caller = document.getElementById("new_account");
	const accounts = document.getElementById("accounts").children[0].children;
	if (!enterKeyPress(event)) {
		// NOTE: accounts node children has been swapped so taking the 0-th index
		for (let i = 0; i < accounts.length; i++) {
			// div->p
			accounts[i].style.display = (
				accounts[i].children[0].innerText !== caller.value
			) ? "none" : "";
		}
		return false;
	}
	let create_new_account = true;
	for (let i = 0; i < accounts.length; i++) {
		// div->p
		accounts[i].style.display = "";
		if (accounts[i].children[0].innerText === caller.value) {
			create_new_account = false;
		}
	}
	if (caller.value === "") {
		caller.style.display = "none";
		document.getElementById("account_select").style.display = "";
		return false;
	}
	if (create_new_account) {
		createNewAccountNode(caller.value);
		// If adding more than 1 accounts
		caller.value = "";
	}
}

function selectAccount() {
	const select = document.getElementById("account_select");
	const selected_account = select.options[select.selectedIndex];
	if (selected_account.value !== "") {
		// display *input tag to create a new account
		let new_account_input = document.getElementById("new_account");
		new_account_input.setAttribute("maxlength", selected_account.getAttribute("maxlength"));
		new_account_input.setAttribute("placeholder", selected_account.innerText);
		select.style.display = "none";
		new_account_input.style.display = "";
		// select was clicked so focusing
		new_account_input.focus();
		// swap accounts node children
		const parent_node = document.getElementById("accounts");
		const parent_node_children = parent_node.children;
		// NOTE: iterates all tags
		let swap_index = 0;
		let swap_with = undefined;
		for (let i = 0; i < parent_node_children.length; i++) {
			if (parent_node_children[i].id === selected_account.value) {
				swap_index = i;
				swap_with = parent_node_children[i];
				break;
			}
		}
		// NOTE: swapped with 0-th index
		if (swap_index) {
			parent_node.insertBefore(swap_with, parent_node_children[0]);
		}
	}
}
