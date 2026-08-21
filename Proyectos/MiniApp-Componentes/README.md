# MiniApp con componentes (framework)

**Estado:** Por hacer · **Objetivo:** practicar UI con framework y componentes, sin reinventar el DOM a mano.

## Idea del proyecto (elige o adapta)

Una **lista de habitos diarios** muy simple:
- Ver habitos
- Marcar uno como hecho hoy
- Añadir un habito nuevo
- Borrar un habito

Nada de backend. Estado en memoria (o `localStorage` si te animas).

## Stack sugerido (lo montas TU)

```bash
npm create vite@latest . -- --template react
npm install
npm run dev
```

Puedes usar React, Vue o Svelte. Lo importante: **componentes**, no un solo archivo gigante.

## Componentes a crear (placeholders)

| Componente | Responsabilidad |
|------------|-----------------|
| `App` | Monta la app y el estado principal |
| `Header` | Titulo + contador de hechos hoy |
| `HabitForm` | Input + boton para añadir |
| `HabitList` | Lista de `HabitItem` |
| `HabitItem` | Un habito: nombre, checkbox, borrar |

## Reglas de aprendizaje

- El codigo lo escribes tu, a mano.
- Si no entiendes un concepto (props, estado, eventos), pregunta: se explica, no se pega la solucion.
- Empieza por maquetar componentes vacios; luego conecta datos.

## Orden recomendado

1. Crear el proyecto Vite + React (o el framework que elijas)
2. Crear los archivos de componentes vacios
3. Hacer que `App` renderice `Header` + `HabitForm` + `HabitList`
4. Añadir estado y pasar props
5. Wire de eventos (añadir / toggle / borrar)
