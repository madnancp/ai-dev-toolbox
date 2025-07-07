import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { TaskCrud } from "@/services/task.service";
import { TaskPriority } from "@/types/shared";
import { Label } from "@radix-ui/react-label";
import { useEffect, useState } from "react";

type Prop = {
  onAdd: () => void
}

const TaskCreateForm = (prop: Prop) => {

  const [taskName, setTaskName] = useState<string>("")
  const [taskDescription, setTaskDescription] = useState<string>("")
  const [taskPriority, setTaskPriority] = useState<TaskPriority>(TaskPriority.Medium)
  const [taskNameError, setTaskNameError] = useState<string | null>(null)


  const handleTaskForm = async (e: React.FormEvent) => {
    e.preventDefault()
    if (taskName === "") {
      setTaskNameError("please enter a task name")
      return
    }

    const result = await TaskCrud.createTask(
      { name: taskName, description: taskDescription, priority: taskPriority }
    )
    console.log(result)

    prop.onAdd()

    console.log({
      name: taskName,
      description: taskDescription,
      priority: taskPriority
    })
    setTaskName("")
    setTaskDescription("")
    setTaskPriority(TaskPriority.Medium)
  }
  return (


    <form className="bg-gray-700/50 p-5 flex flex-col rounded-lg" onSubmit={handleTaskForm}>
      <h1 className="text-xl capitalize font-bold text-center">add your todos.</h1>
      <div className="mb-3">
        <Input
          type="text"
          placeholder="Task name"
          value={taskName}
          onChange={(e) => { setTaskName(e.target.value); setTaskNameError(null) }}
        />
        {taskNameError && (
          <span className="text-red-500 text-sm">{taskNameError}</span>
        )}
      </div>

      <Input
        type="text"
        placeholder="Description"
        className="mb-3"
        value={taskDescription}
        onChange={(e) => setTaskDescription(e.target.value)}
      />

      <Label className="text-sm text-gray-300 mb-1">Priority:</Label>
      <RadioGroup value={taskPriority} className="flex justify-evenly mb-3" onValueChange={(value: TaskPriority) => setTaskPriority(value)}>
        <div className="flex justify-center items-center gap-2">
          <RadioGroupItem value={TaskPriority.Low} id="p1" />
          <Label htmlFor="p1">Low</Label>
        </div>

        <div className="flex justify-center items-center gap-2">
          <RadioGroupItem value={TaskPriority.Medium} id="p2" />
          <Label htmlFor="p2">Medium</Label>
        </div>

        <div className="flex justify-center items-center gap-2">
          <RadioGroupItem value={TaskPriority.High} id="p3" />
          <Label htmlFor="p3">High</Label>
        </div>
      </RadioGroup>

      <Button>Add new Task</Button>
    </form>

  )
}

export default TaskCreateForm;
