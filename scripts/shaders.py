from OpenGL.GL import *
from OpenGL.GL import shaders
import numpy as np

class ShaderManager:
    def __init__(self):
        self.shader_programs = {}
        self.current_shader = None
    
    def load_shader(self, name, vertex_source, fragment_source):
        """
        Compila y almacena un nuevo shader program
        """
        try:
            vertex_shader = shaders.compileShader(vertex_source, GL_VERTEX_SHADER)
            fragment_shader = shaders.compileShader(fragment_source, GL_FRAGMENT_SHADER)
            
            program = shaders.compileProgram(vertex_shader, fragment_shader)
            self.shader_programs[name] = program
            
            # Limpiar los shaders individuales
            glDeleteShader(vertex_shader)
            glDeleteShader(fragment_shader)
            
            return program
        except Exception as e:
            print(f"Error loading shader {name}: {str(e)}")
            return None
    
    def use_shader(self, name):
        """
        Activa un shader específico
        """
        if name in self.shader_programs:
            self.current_shader = self.shader_programs[name]
            glUseProgram(self.current_shader)
        else:
            print(f"Shader {name} not found!")
    
    def stop_shader(self):
        """
        Desactiva el shader actual
        """
        glUseProgram(0)
        self.current_shader = None
    
    def get_uniform_location(self, name, uniform_name):
        """
        Obtiene la ubicación de una variable uniform
        """
        if name in self.shader_programs:
            return glGetUniformLocation(self.shader_programs[name], uniform_name)
        return -1
    
    def set_uniform_1f(self, location, value):
        """
        Establece un valor float uniform
        """
        glUniform1f(location, value)
    
    def set_uniform_3f(self, location, x, y, z):
        """
        Establece un valor vec3 uniform
        """
        glUniform3f(location, x, y, z)
    
    def set_uniform_4f(self, location, x, y, z, w):
        """
        Establece un valor vec4 uniform
        """
        glUniform4f(location, x, y, z, w)
    
    def set_uniform_matrix4fv(self, location, matrix):
        """
        Establece una matriz 4x4 uniform
        """
        glUniformMatrix4fv(location, 1, GL_FALSE, matrix)

# Definición de shaders predefinidos
class ShaderLibrary:
    @staticmethod
    def get_outline_shader():
        vertex_shader = """
        #version 330 core
        layout (location = 0) in vec3 position;
        layout (location = 1) in vec3 normal;
        
        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;
        uniform float outline_thickness;
        
        void main()
        {
            vec3 scaled_position = position + normal * outline_thickness;
            gl_Position = projection * view * model * vec4(scaled_position, 1.0);
        }
        """

        fragment_shader = """
        #version 330 core
        uniform vec4 outline_color;
        
        out vec4 FragColor;
        
        void main()
        {
            FragColor = outline_color;
        }
        """
        
        return vertex_shader, fragment_shader