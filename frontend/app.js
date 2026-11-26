const API_BASE_URL = "http://localhost:8000"; // Replace with your HTTPS backend URL when deployed.
const form = document.querySelector("#chat-form");
const input = document.querySelector("#message");
const messages = document.querySelector("#messages");
const send = document.querySelector("#send");
function addBubble(text, who) { const node=document.createElement("article"); node.className=`bubble ${who}`; const label=document.createElement("b"); label.textContent=who==="user"?"YOU":"JARVIS"; const body=document.createElement("p"); body.textContent=text; node.append(label,body); messages.append(node); messages.scrollTop=messages.scrollHeight; return body; }
form.addEventListener("submit", async event => { event.preventDefault(); const message=input.value.trim(); if(!message)return; addBubble(message,"user"); input.value=""; send.disabled=true; const reply=addBubble("Thinking…","assistant"); try { const response=await fetch(`${API_BASE_URL}/api/chat`,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({message})}); if(!response.ok)throw new Error(`API returned ${response.status}`); const data=await response.json(); reply.textContent=data.reply; } catch(error) { reply.textContent=`Couldn't reach the JARVIS backend. ${error.message}. Check backend and API_BASE_URL.`; } finally { send.disabled=false; messages.scrollTop=messages.scrollHeight; } });
if("serviceWorker" in navigator && location.protocol.startsWith("http")) navigator.serviceWorker.register("./sw.js").catch(()=>{});
