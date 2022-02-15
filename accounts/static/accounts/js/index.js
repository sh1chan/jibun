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
  div.className = "card";
  // NOTE: accounts node children has been swapped so taking the 0-th index
  const parent_node = document.getElementById("accounts").children[0];
  parent_node.insertBefore(div, parent_node.children[0]);
}

function registerNewAccount(event) {
  if (!enterKeyPress(event)) {
    return false;
  }

  const caller = document.getElementById("new_account");

  if (caller.value === "") {
    return false;
  }

  createNewAccountNode(caller.value);
  // If adding more than 1 accounts
  caller.value = "";
}
