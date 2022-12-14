import * as React from "react"
import { CountProvider, useCount } from "./count-context"
function Counter() {
    const [count, setCount] = useCount()
    const increment = () => setCount((c) => c + 1)
    return <button onClick={increment}>{count}</button>
}
function CountDisplay() {
    const [count] = useCount()
    return <div>El contador actual es {count}</div>
}
function CountPage() {
return (
        <div>
            <CountProvider>
                <CountDisplay />
                <Counter />
            </CountProvider>
        </div>
    )
}