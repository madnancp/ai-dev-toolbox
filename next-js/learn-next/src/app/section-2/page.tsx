"use client"
import TaskCard from "@/components/custom/TaskCard";
import Counter from "./components/Counter";
import CharCounterForm from "./components/forms/CharCounter";
import FeedBackForm from "./components/forms/FeedBack";
import TodoForm from "./components/forms/TodoForm";
import JokeFetcher from "./components/JokeFecther";
import Like from "./components/Like";
import LiveClock from "./components/LiveClock";
import ThemeSwitcher from "./components/ThemeSwitcher";
import Toggler from "./components/Toggler";
import { Task } from "@/types/shared";
import { useState } from "react";

const SectionTwo = () => {

  const [localDb, setLocalDb] = useState<Task[]>([]);

  const handleNewTask = (newTask: Task) => {
    setLocalDb(localDb => [...localDb, newTask])
  }

  return (
    <div className="h-auto">
      <div className="h-screen mb-20">
        <h1 className="font-bold text-3xl text-center">Learn useState</h1>
        <div className="grid grid-cols-2 gap-3 h-full">
          <Counter />
          <Toggler />
          <Like />
          <ThemeSwitcher />
        </div>
      </div>

      <div className="h-80 mb-20">
        <h1 className="font-bold text-3xl text-center">Learn useEffect</h1>
        <div className="grid grid-cols-2 gap-3 h-full">
          <JokeFetcher />
          <LiveClock />
        </div>
      </div>

      <div className="h-80 mb-20">
        <h1 className="font-bold text-3xl text-center">Learn Form Handling</h1>
        <div className="grid grid-cols-2 gap-3 h-full">
          <FeedBackForm />
          <CharCounterForm />
        </div>
      </div>

      <div className="h-screen">
        <h1 className="font-bold text-3xl text-center">The Lazy Todo App</h1>
        <div className="h-full border rounded-3xl shadow">
          <TodoForm onAdd={handleNewTask} />
          <div className="grid grid-cols-3 gap-5 items-center px-5 mt-5">
            {localDb.map((each) => (
              <TaskCard key={each.id} name={each.name} descreption={each.descreption} priority={each.priority} />
            ))}
          </div>
        </div>
      </div>

    </div>
  )
}

export default SectionTwo;
