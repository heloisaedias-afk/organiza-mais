const API="http://127.0.0.1:5000/api",$=id=>document.getElementById(id);
let estudantes=[],materias=[],atividades=[];
async function api(url,options={}){const r=await fetch(API+url,{headers:{"Content-Type":"application/json"},...options});const d=await r.json().catch(()=>({}));if(!r.ok)throw Error(d.erro||"Erro na requisição.");return d}
function msg(t){$("msg").textContent=t;$("msg").style.display="block";setTimeout(()=>$("msg").style.display="none",3200)}
function esc(v){return String(v??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}
function dataBR(v){if(!v)return "";let [y,m,d]=v.slice(0,10).split("-");return `${d}/${m}/${y}`}
async function carregar(){try{[estudantes,materias,atividades]=await Promise.all([api("/estudantes"),api("/materias"),api("/atividades")]);render()}catch(e){msg(e.message)}}
function render(){
 $("estudanteInfo").textContent=estudantes.length?"Cadastrados: "+estudantes.map(x=>x.nome).join(", "):"Cadastre o estudante antes de adicionar matérias.";
 $("estudanteMateria").innerHTML='<option value="">Selecione</option>'+estudantes.map(x=>`<option value="${x.id_estudante}">${esc(x.nome)}</option>`).join("");
 $("materiaAtividade").innerHTML='<option value="">Selecione</option>'+materias.map(x=>`<option value="${x.id_materia}">${esc(x.nome_materia)}</option>`).join("");
 $("materias").innerHTML=materias.map(x=>`<span class="chip">${esc(x.nome_materia)} • ${esc(x.nome_estudante)}</span>`).join("");
 const filtro=$("filtro").value,vis=atividades.filter(x=>!filtro||x.status===filtro);
 $("atividades").innerHTML=vis.length?vis.map(x=>`<article class="item"><div><h3>${esc(x.titulo)} <span class="tag ${x.status==="Concluída"?"done":""}">${x.status}</span></h3><p>${esc(x.nome_materia)} • ${esc(x.tipo)} • Entrega: ${dataBR(x.data_entrega)}</p><p>${esc(x.descricao)}</p></div><div class="actions"><button class="alt" onclick="mudarStatus(${x.id_atividade},'${x.status==="Pendente"?"Concluída":"Pendente"}')">${x.status==="Pendente"?"Concluir":"Reabrir"}</button><button class="alt" onclick="editar(${x.id_atividade})">Editar</button><button class="del" onclick="excluir(${x.id_atividade})">Excluir</button></div></article>`).join(""):"<p class='muted'>Nenhuma atividade cadastrada.</p>";
 $("total").textContent=atividades.length;$("pendentes").textContent=atividades.filter(x=>x.status==="Pendente").length;$("feitas").textContent=atividades.filter(x=>x.status==="Concluída").length;
}
$("formEstudante").addEventListener("submit",async e=>{e.preventDefault();try{await api("/estudantes",{method:"POST",body:JSON.stringify({nome:$("nomeEstudante").value})});e.target.reset();msg("Estudante cadastrado!");await carregar()}catch(x){msg(x.message)}});
$("formMateria").addEventListener("submit",async e=>{e.preventDefault();try{await api("/materias",{method:"POST",body:JSON.stringify({nome_materia:$("nomeMateria").value,id_estudante:Number($("estudanteMateria").value)})});e.target.reset();msg("Matéria cadastrada!");await carregar()}catch(x){msg(x.message)}});
$("formAtividade").addEventListener("submit",async e=>{e.preventDefault();try{await api("/atividades",{method:"POST",body:JSON.stringify({titulo:$("titulo").value,descricao:$("descricao").value,tipo:$("tipo").value,data_entrega:$("data").value,id_materia:Number($("materiaAtividade").value),status:"Pendente"})});e.target.reset();msg("Atividade cadastrada!");await carregar()}catch(x){msg(x.message)}});
$("filtro").addEventListener("change",render);
async function mudarStatus(id,status){try{await api(`/atividades/${id}/status`,{method:"PATCH",body:JSON.stringify({status})});await carregar()}catch(e){msg(e.message)}}
async function excluir(id){if(!confirm("Deseja excluir esta atividade?"))return;try{await api(`/atividades/${id}`,{method:"DELETE"});msg("Atividade excluída.");await carregar()}catch(e){msg(e.message)}}
async function editar(id){const a=atividades.find(x=>x.id_atividade===id);const titulo=prompt("Título:",a.titulo);if(titulo===null)return;const descricao=prompt("Descrição:",a.descricao);if(descricao===null)return;const data_entrega=prompt("Data (AAAA-MM-DD):",a.data_entrega);if(data_entrega===null)return;try{await api(`/atividades/${id}`,{method:"PUT",body:JSON.stringify({...a,titulo,descricao,data_entrega})});msg("Atividade atualizada.");await carregar()}catch(e){msg(e.message)}}
carregar();
