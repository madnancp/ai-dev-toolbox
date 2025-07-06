"use client"


import { TaskCrud } from "@/services/task.service";
import { ITask } from "@/types/shared";
import { useEffect, useState } from "react";

const Todo = () => {
  const [tasks, setTasks] = useState<ITask[]>([])

  useEffect(() => {
    const call = async () => {
      const data = await TaskCrud.getAllTasks()
      setTasks(data);
    }
    call()
  }, [])
  return (
    <div className="text-white">
      <ul>
        {tasks && (
          tasks.map((each) => (
            <li key={each.id}>{each.name} : {each.description} : {each.priority}</li>
          )
          ))}
      </ul>
    </div>
  )
}

export default Todo;
