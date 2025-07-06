import { ITask, ITaskCreate } from "@/types/shared";


export class TaskCrud {
	static readonly NEXT_PUBLIC_API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

	static async getAllTasks(): Promise<ITask[] | []> {
		try {
			const response = await fetch(`${this.NEXT_PUBLIC_API_BASE_URL}/tasks`, {
				method: "GET"
			})
			const data: ITask[] = await response.json()
			return data;
		} catch (err) {
			console.log(err)
			return []
		}

	}

	static async getTask(id: string): Promise<ITask | null> {
		try {

			const response = await fetch(`${this.NEXT_PUBLIC_API_BASE_URL}/task/${id}`, {
				method: "GET"
			})
			const data: ITask = await response.json()
			return data;


		} catch (err) {
			console.log(err)
			return null
		}

	}

	static async createTask(task: ITaskCreate): Promise<ITask | null> {
		try {
			const response = await fetch(`${this.NEXT_PUBLIC_API_BASE_URL}/task`, {
				method: "POST",
				credentials: "include",
				body: JSON.stringify(task),
				headers: {
					"Content-Type": "application/json"
				}
			})
			const data: ITask = await response.json()
			return data

		} catch (err) {
			console.error(err)
			return null
		}

	}

}
