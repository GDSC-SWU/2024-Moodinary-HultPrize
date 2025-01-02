package com.example.moodinary.ui.home

import android.os.Bundle
import android.text.SpannableString
import android.text.Spanned
import android.text.style.ForegroundColorSpan
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.content.ContextCompat
import com.example.moodinary.R
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
        spanColor()
        dateFormat()
    }

    private fun dateFormat() {
        val currentDate = Date()
        val dateFormat = SimpleDateFormat("yyyy.MM.dd", Locale.getDefault())
        val formattedDate = dateFormat.format(currentDate)
        binding.tvDate.text = formattedDate
    }

    private fun spanColor() {
        val spannableString = SpannableString(binding.tvDiaryCreateTitle.text)
        val colorSpan =
            ForegroundColorSpan(ContextCompat.getColor(requireContext(), R.color.purple))
        spannableString.setSpan(colorSpan, 8, 18, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE)
        binding.tvDiaryCreateTitle.text = spannableString
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}