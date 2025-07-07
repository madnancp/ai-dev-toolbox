"use client"
import { TaskCrud } from "@/services/task.service";
import { ITask } from "@/types/shared";
import { useEffect, useState } from "react";
import TaskCreateForm from "./forms/TaskForm";
import TaskDisplayCard from "./components/TaskCard";

const Todo = () => {
  const [tasks, setTasks] = useState<ITask[]>([])

  const fetchTasks = async () => {
    const data = await TaskCrud.getAllTasks()
    setTasks(data);
  }

  useEffect(() => {
    fetchTasks()
  }, [])

  const handleOnTaskChange = () => {
    fetchTasks()
  }
  return (
    <div className="flex justify-center h-screen">
      <div className="max-w-96 w-full max-h-9/10 h-full  my-8 ">
        <TaskCreateForm onAdd={handleOnTaskChange} />
        <div className="bg-gray-700/50 rounded-md mt-4 max-h-3/5 overflow-x-scroll p-5 flex flex-col gap-5">
          {tasks.map((each) => (
            <TaskDisplayCard key={each.id} id={each.id} name={each.name} descreption={each.description} priority={each.priority} handleTaskEdit={handleOnTaskChange} />
          ))}
        </div>
      </div>
    </div>
  )
}

export default Todo;
