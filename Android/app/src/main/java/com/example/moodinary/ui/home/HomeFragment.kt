package com.example.moodinary.ui.home

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.example.moodinary.databinding.FragmentHomeBinding
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class HomeFragment : Fragment() {

    private var _binding : FragmentHomeBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        setLayout()

    }

    private fun setLayout() {
        binding.btnHomeDiaryWrite.setOnClickListener {
            val action = HomeFragmentDirections.actionHomeToDiary()
            findNavController().navigate(action)
        }
        setDateFormat()
    }

    private fun setDateFormat() {
        val currentDate = Date()
        val dateFormat = SimpleDateFormat("M월 d일 EEEE", Locale.KOREAN)
        val formattedDate = dateFormat.format(currentDate)
        binding.tvHomeDate.text = formattedDate
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}