<script setup lang="ts">
import { Delete, ArrowUp, ArrowDown } from "@element-plus/icons-vue";
import { onMounted, ref } from "vue";
import axios from 'axios';

const newTask = ref<string>("");
const tasks = ref<{ id: number; description: string }[]>([]);
const isEditing = ref<boolean[]>([]);

const fetchTasks = async () => {
  try {
    const response = await axios.get('api/tasks');
    console.log('response:', response);
    tasks.value = response.data;
    isEditing.value = Array(tasks.value.length).fill(false);
  } catch (error) {
    console.error('Failed to fetch tasks:', error);
  }
};

const addTask = async () => {
  if (newTask.value.trim() !== '') {
    try {
      const response = await axios.post('api/tasks', {
        description: newTask.value,
      });
      tasks.value.push(response.data);
      newTask.value = '';
    } catch (error) {
      console.error('Failed to add task:', error);
    }
  }
};

const removeTask = async (index: number) => {
  try {
    const taskId = tasks.value[index].id;
    await axios.delete(`api/tasks/${taskId}`);
    tasks.value.splice(index, 1);
  } catch (error) {
    console.error('Failed to remove task:', error);
  }
};

const editTask = async (index: number) => {
  isEditing.value[index] = true;
};

const updateTask = async (index: number) => {
  const taskId = tasks.value[index].id;  // 取得當前任務的 ID
  const updatedDescription = tasks.value[index].description;  // 取得當前修改後的描述
  
  try {
    // 發送 PUT 請求更新後端的任務
    await axios.put(`api/tasks/${taskId}`, {
      description: updatedDescription
    });
    
    // 標記編輯狀態
    isEditing.value[index] = false;
  } catch (error) {
    console.error('Failed to update task:', error);
  }
};

const moveTaskUp = async (index: number) => {
  if (index > 0) {
    const taskId = tasks.value[index].id;
    try {
      // 發送 PATCH 請求通知後端將任務向上移動
      await axios.patch(`api/tasks/move/${taskId}`, { direction: 'up' });

      // 前端更新任務順序
      const temp = tasks.value[index];
      tasks.value[index] = tasks.value[index - 1];
      tasks.value[index - 1] = temp;
    } catch (error) {
      console.error('Failed to move task up:', error);
    }
  }
};

const moveTaskDown = async (index: number) => {
  if (index < tasks.value.length - 1) {
    const taskId = tasks.value[index].id;
    try {
      // 發送 PATCH 請求通知後端將任務向下移動
      await axios.patch(`api/tasks/move/${taskId}`, { direction: 'down' });

      // 前端更新任務順序
      const temp = tasks.value[index];
      tasks.value[index] = tasks.value[index + 1];
      tasks.value[index + 1] = temp;
    } catch (error) {
      console.error('Failed to move task down:', error);
    }
  }
};

onMounted(fetchTasks);
</script>

<template>
  <div style="padding: 20px; min-height: 100vh; width: 100%">
    <el-container style="width: 80vw; margin: auto">
      <el-header>
        <h1>Todo List</h1>
      </el-header>
      <el-main style="overflow-x: hidden">
        <el-form @submit.prevent="addTask" inline style="width: 100%">
          <el-form-item style="width: 80%">
            <el-input v-model="newTask" placeholder="Add a new task" />
          </el-form-item>
          <el-form-item style="width: 12%">
            <el-button type="primary" @click="addTask" style="width: 100%"
              >Add</el-button
            >
          </el-form-item>
        </el-form>

        <transition-group name="list" tag="div">
          <el-card
            style="margin-top: 20px"
            v-for="(task, index) in tasks"
            :key="task.id"
          >
            <div class="task-item">
              <span v-if="!isEditing[index]">{{ index + 1 }}. {{ task.description }}</span>
              <el-input
                v-else
                v-model="tasks[index].description"
                size="mini"
                style="width: 55%"
              />
              <div class="button-group">
                <el-button
                  v-if="!isEditing[index]"
                  @click="editTask(index)"
                  type="warning"
                  size="mini"
                >
                  Edit
                </el-button>
                <el-button
                  v-else
                  @click="updateTask(index)"
                  type="success"
                  size="mini"
                >
                  Save
                </el-button>
                <el-button
                  @click="moveTaskUp(index)"
                  type="primary"
                  size="mini"
                  :icon="ArrowUp"
                  :disabled="index === 0 || isEditing[index]"
                >
                  Up
                </el-button>
                <el-button
                  @click="moveTaskDown(index)"
                  type="primary"
                  size="mini"
                  :icon="ArrowDown"
                  :disabled="index === tasks.length - 1 || isEditing[index]"
                >
                  Down
                </el-button>
                <el-button
                  @click="removeTask(index)"
                  type="danger"
                  size="mini"
                  :icon="Delete"
                >
                  Delete
                </el-button>
              </div>
            </div>
          </el-card>
        </transition-group>
      </el-main>
    </el-container>
  </div>
</template>

<style scoped>
.mt-4 {
  margin-top: 16px;
}

.task-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.3s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>
